import torch
import cv2
import time
import argparse
import timeit
import numpy as np
import matplotlib
import numpy as np
from dtw import dtw
import statistics
import json
import os
##############
#도커파일에서 실제로 돌아가는 코드
##############
matplotlib.use('Agg')

from movenet.models.model_factory import load_model
from movenet.utils import read_cap, draw_skel_and_kp, new_draw_skel_and_kp
# cropping related functions
# from movenet.utils import init_crop_region, determine_crop_region

# videopose
from poseaug.models.model_factory import load_model as load_model_pose
from poseaug.utils import create_2d_data, show3Dpose, create_new_skel

parser = argparse.ArgumentParser()
### TODO : model 변경 시 movenet.py에서 get_pose_net 함수 파라미터 변경해야함
parser.add_argument('--model', type=str, default="movenet_lightning", choices=["movenet_lightning", "movenet_thunder"])
parser.add_argument('--cam_id', type=int, default=0)
parser.add_argument('--cam_width', type=int, default=1000)
parser.add_argument('--cam_height', type=int, default=1000)
parser.add_argument('--conf_thres', type=float, default=0.05)
parser.add_argument('--cropping', action='store_false')
parser.add_argument('--vid_path', type=str, required=True, help='Path to video file')
args = parser.parse_args()
if args.model == "movenet_lightning":
    args.size = 192
    args.ft_size = 48
else:
    args.size = 256
    args.ft_size = 64

video_filename = os.path.basename(args.vid_path)
json_filename = os.path.splitext(video_filename)[0] + ".json"
output_dir = "./sym/data/output"

args.vid_path = os.path.join("/app/sym/data/", args.vid_path)
print('동영상zzz', args.vid_path)


def kpt_noramlizations(kpt_numpy, height, width, kpt_list, kpt_with_conf):
    kpt_numpy_y = kpt_numpy[:, 0] * height
    kpt_numpy_x = kpt_numpy[:, 1] * width
    kpt_numpy_yx = kpt_numpy[:, :2]

    if len(kpt_list) == 0:
        kpt_list.append(kpt_numpy_yx)

    else:
        y, x = kpt_list[-1].T

        if np.mean(y) < 1:
            y = y * height
        else:
            y = y

        if np.mean(x) < 1:
            x = x * width
        else:
            x = x

        point_noise_y = np.abs(y - kpt_numpy_y)
        point_noise_x = np.abs(x - kpt_numpy_x)

        for i in range(len(point_noise_y)):
            if point_noise_y[i] + point_noise_x[i] < 7:
                kpt_numpy[:, 0][i] = kpt_list[-1][:, 0][i] / height
                kpt_numpy[:, 1][i] = kpt_list[-1][:, 1][i] / width

            else:
                kpt_numpy[:, 0][i] = kpt_numpy[:, 0][i]
                kpt_numpy[:, 1][i] = kpt_numpy[:, 1][i]

                kpt_list.append(kpt_numpy_yx)
                del kpt_list[0]

    for a in range(len(kpt_with_conf)):
        # print('kpt_with_conf[:,0][a]',kpt_with_conf[:,0][a])
        if kpt_with_conf[:, 0][a] < 0.01:
            kpt_with_conf[:, 0][a] = kpt_with_conf[:, 0][a] * height
    for b in range(len(kpt_with_conf)):
        if kpt_with_conf[:, 1][b] < 0.01:
            kpt_with_conf[:, 1][b] = kpt_with_conf[:, 1][b] * width
    kpt_with_conf = torch.Tensor(kpt_with_conf)

    return kpt_with_conf


def main():
    model = load_model(args.model).eval()
    pose_aug = load_model_pose().eval()
    print(args.vid_path)

    cap = cv2.VideoCapture(args.vid_path)  # 입력 동작 영상
    cap.set(3, args.cam_width)
    cap.set(4, args.cam_height)

    start = time.time()
    pose_data = {"frames": []}
    frame_count = 0

    kpt_list = []

    while True:

        # print(frame_count)

        input_image, display_image = read_cap(
            cap, size=args.size)  # input_image : (1, 192, 192, 3), display_image : (480, 640, 3)

        if input_image is None:  # 영상이 끝났을 경우 종료
            break
        ### 결과 영상 크기 조절
        if display_image.shape[0] != 480 or display_image.shape[1] != 640:
            display_image = cv2.resize(display_image, (640, 480))
            # print('영상 조절됨')

        with torch.no_grad():
            input_image = torch.Tensor(input_image)  # .cuda(), # torch.Size([1, 192, 192, 3])
            kpt_with_conf = model(input_image)[0, 0, :, :]  # torch.Size([17, 3])

            height, width, _ = display_image.shape
            ## User
            kpt_numpy = kpt_with_conf.numpy()
            kpt_with_conf = kpt_noramlizations(kpt_numpy, height, width, kpt_list, kpt_with_conf)

            inputs_2d = create_2d_data(kpt_with_conf)  # torch.Size([1, 16, 2])
            outputs_3d = pose_aug(inputs_2d).squeeze(0).numpy()  # torch.Size([1, 16, 3]) # 3차원 결과
        joint_data = [{'x': float(x),
                       'y': float(y),
                       'z': float(z)} for x, y, z in outputs_3d]
        pose_data["frames"].append({"frame": frame_count, "joints": joint_data})

        frame_count += 1

    json_path = os.path.join(output_dir, json_filename)

    with open(json_path, "w") as f:
        json.dump(pose_data, f, indent=4)

    print(f"✅ JSON 저장 완료: {json_filename}")

    cap.release()
    cv2.destroyAllWindows()
    print(json_path)


if __name__ == "__main__":
    print("현재 작업 디렉토리:", os.getcwd())
    main()