from __future__ import absolute_import, division
from typing import Mapping

import numpy as np
# import matplotlib.pyplot as plt
# from mpl_toolkits.mplot3d import Axes3D

import torch



# Joints in H3.6M -- data has 32 joints, but only 17 that move; these are the indices.
H36M_NAMES = [''] * 32
H36M_NAMES[0] = 'Hip'  # mid of 11 and 12
H36M_NAMES[1] = 'RHip'  # 12
H36M_NAMES[2] = 'RKnee'  # 14
H36M_NAMES[3] = 'RFoot'  # 16
H36M_NAMES[6] = 'LHip'  # 11
H36M_NAMES[7] = 'LKnee'  # 13
H36M_NAMES[8] = 'LFoot'  # 15
H36M_NAMES[12] = 'Spine'  # mid of 'Hip' and 'Thorax'
H36M_NAMES[13] = 'Thorax'  # mid of 5 and 6
# H36M_NAMES[14] = 'Neck/Nose' # None
H36M_NAMES[15] = 'Head'  # mid of 1 and 2
H36M_NAMES[17] = 'LShoulder'  # 5
H36M_NAMES[18] = 'LElbow'  # 7
H36M_NAMES[19] = 'LWrist'  # 9
H36M_NAMES[25] = 'RShoulder'  # 6
H36M_NAMES[26] = 'RElbow'  # 8
H36M_NAMES[27] = 'RWrist'  # 10

MAPPING_COCO_H36M = [0, 12, 14, 16, 11, 13, 15, 0, 0, 0, 5, 7, 9, 6, 8, 10]


# Dictionary that maps from joint names to keypoint indices.
KEYPOINT_DICT = {
    'nose': 0,
    'left_eye': 1,
    'right_eye': 2,
    'left_ear': 3,
    'right_ear': 4,
    'left_shoulder': 5,
    'right_shoulder': 6,
    'left_elbow': 7,
    'right_elbow': 8,
    'left_wrist': 9,
    'right_wrist': 10,
    'left_hip': 11,
    'right_hip': 12,
    'left_knee': 13,
    'right_knee': 14,
    'left_ankle': 15,
    'right_ankle': 16
}


def image_coordinates(X, w, h):
    assert X.shape[-1] == 2

    # Reverse camera frame normalization
    return (X + [1, h / w]) * w / 2


def normalize_screen_coordinates(X, w, h):
    assert X.shape[-1] == 2 # X가 2차원이라는 가정 설명문

    # Normalize so that [0, w] is mapped to [-1, 1], while preserving the aspect ratio
    # return X / w * 2 - [1, h / w]
    return X / w * 2 - 1 # 원래 사용

def create_new_skel(keypoints_with_conf, w=640, h=480):

    # convert to pixel space
    keypoints = keypoints_with_conf[:, :2] * w  ## keypoints_with_conf에서 x,y좌표만 사용하고, confidence 좌표는 사용안함, ## (17,3)
    inputs_2d = torch.zeros((16, 2))
    inputs_2d = keypoints[MAPPING_COCO_H36M] # (16,2)

    inputs_2d[0] = (keypoints[11, :] + keypoints[12, :]) / 2.0 # 엉덩이 중심
    inputs_2d[8] = (keypoints[5, :] + keypoints[6, :]) / 2.0 # 어깨 중심
    inputs_2d[9] = (keypoints[1, :] + keypoints[2, :]) / 2.0 # 눈 중심
    inputs_2d[7] = (inputs_2d[0] + inputs_2d[8]) / 2.0 # 엉덩이 중심과 어깨 중심의 중앙

    # print('inputs_2dasdasdasd',inputs_2d / w)

    # keypoint confidence shape 변환 (17개 => 16개)
    confid = keypoints_with_conf[:, 2]
    confid_2d = torch.zeros((16, 1))
    confid_2d = confid[MAPPING_COCO_H36M]
    confid_2d[0] = (confid[11] + confid[12]) / 2.0
    confid_2d[8] = (confid[5] + confid[6]) / 2.0 # 어깨 중심
    confid_2d[9] = (confid[1] + confid[2]) / 2.0 # 눈 중심
    confid_2d[7] = (confid_2d[0] + confid_2d[8]) / 2.0 # 엉덩이 중심과 어깨 중심의 중앙


    # inputs_2d_numpy = inputs_2d.numpy()
    # confid_2d_numpy = confid_2d.numpy()

    inputs_2d = inputs_2d / w


    # new_kpt_with_conf = np.dstack((inputs_2d[:, 1], inputs_2d[:, 0], confid_2d))
    # new_kpt_with_conf = normalize_screen_coordinates(new_kpt_with_conf, w, h) # 상대죄표 출력
    # new_kpt_with_conf = new_kpt_with_conf.squeeze(0)

    return inputs_2d, confid_2d

def create_2d_data(keypoints_with_conf, w=640, h=480):
    '''
    Assume `keypoints` comes from the MoveNet, which is scaled to [0, 1]; The image size is [1000, 1000].
    1. In this functions, we first do the keypoints convertion from COCO style to H36M/MPII style.
    2. Then we do the normailize screen coodinates using function `normalize_screen_coordinates`.
    '''

    # convert to pixel space
    keypoints = keypoints_with_conf[:, :2] * w  ## keypoints_with_conf에서 x,y좌표만 사용하고, confidence 좌표는 사용안함, ## (17,3)
    inputs_2d = torch.zeros((16, 2))
    inputs_2d = keypoints[MAPPING_COCO_H36M] # (16,2)

    inputs_2d[0] = (keypoints[11, :] + keypoints[12, :]) / 2.0 # 엉덩이 중심
    inputs_2d[8] = (keypoints[5, :] + keypoints[6, :]) / 2.0 # 어깨 중심
    inputs_2d[9] = (keypoints[1, :] + keypoints[2, :]) / 2.0 # 눈 중심
    inputs_2d[7] = (inputs_2d[0] + inputs_2d[8]) / 2.0 # 엉덩이 중심과 어깨 중심의 중앙

    '''
    inputs_2d index별 부위
    [0] : 엉덩이 중심, [1] : 오른쪽 엉덩이, [2] : 오른쪽 무릎. [3] : 오른쪽 발, [4] : 왼쪽 엉덩이, [5] : 왼쪽 무릎, [6] : 왼쪽 발
    [7] : 엉덩이 중심과 어깨 중심의 중앙, [8] : 어깨 중심, [9] : 눈 중심, [10] : 왼쪽 어깨, [11] : 왼쪽 엘보우, [12] : 왼쪽 손목
    [13] : 오른쪽 어깨, [14] : 오른쪽 엘보우, [15] : 오른쪽 손목
    '''

    '''
    다리쪽(스쿼트) skeleton : 0, 1, 2, 3, 4, 5, 6
    [3,3,3,3,3,3,3,0.3,0.3,0.3,0.3,0.3,0.3,0.3,0.3,0.3]
    '''

    inputs_2d = torch.stack((inputs_2d[:,1], inputs_2d[:,0]), dim=1)
    inputs_2d = normalize_screen_coordinates(inputs_2d, w, h) # 상대죄표 출력
    inputs_2d = inputs_2d.view(1, 16, 2)

    return inputs_2d


def show3Dpose(channels, ax, lcolor="#3498db", rcolor="#e74c3c", add_labels=True,
               gt=False,pred=False): # blue, orange  ## lcolor 파란색조, rcolor : 빨간색조
    """
    Visualize a 3d skeleton

    Args
    channels: 96x1 vector. The pose to plot.
    ax: matplotlib 3d axis to draw on
    lcolor: color for left part of the body
    rcolor: color for right part of the body
    add_labels: whether to add coordinate labels
    Returns
    Nothing. Draws on ax.
    """

    #   assert channels.size == len(data_utils.H36M_NAMES)*3, "channels should have 96 entries, it has %d instead" % channels.size
    vals = np.reshape( channels, (16, -1) ) # (16,3) shape

    #     I = np.array([1, 2, 3, 1, 5, 6, 1, 8, 9, 9,
    #                  11, 12, 9, 14, 15])-1  # start points
    #     J = np.array([2, 3, 4, 5, 6, 7, 8, 9, 10, 11,
    #                  12, 13, 14, 15, 16])-1  # end points
    I  = np.array([0,1,2,0,4,5,0,7,8,8,10,11,8,13,14]) # start points
    J  = np.array([1,2,3,4,5,6,7,8,9,10,11,12,13,14,15]) # end points
    LR = np.array([1, 1, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 1, 1], dtype=bool) # 1이 오른쪽

    # Make connection matrix
    for i in np.arange( len(I) ):
        x, y, z = [np.array( [vals[I[i], j], vals[J[i], j]] ) for j in range(3)]
        if gt:
            ax.plot(x,z, -y,  lw=2, c='k')
        #        ax.plot(x,y, z,  lw=2, c='k')

        elif pred:
            ax.plot(x,z, -y,  lw=2, c='r')
        #        ax.plot(x,y, z,  lw=2, c='r')

        ## 모두 else에 해당하는 조건을 가짐
        else:
        #        ax.plot(x,z, -y,  lw=2, c=lcolor if LR[i] else rcolor)
            ax.plot(x, z, -y,  lw=2, c=lcolor if LR[i] else rcolor)

    RADIUS = 1 # space around the subject
    xroot, yroot, zroot = vals[0,0], vals[0,1], vals[0,2]
    ax.set_xlim3d([-RADIUS+xroot, RADIUS+xroot])
    ax.set_ylim3d([-RADIUS+zroot, RADIUS+zroot])
    ax.set_zlim3d([-RADIUS-yroot, RADIUS-yroot])


    if add_labels:
        ax.set_xlabel("x")
        ax.set_ylabel("z")
        ax.set_zlabel("-y")

    # Get rid of the ticks and tick labels
    #  ax.set_xticks([])
    #  ax.set_yticks([])
    #  ax.set_zticks([])
    #
    #  ax.get_xaxis().set_ticklabels([])
    #  ax.get_yaxis().set_ticklabels([])
    #  ax.set_zticklabels([])
#     ax.set_aspect('equal')

    # Get rid of the panes (actually, make them white)
    white = (1.0, 1.0, 1.0, 0.0)
    ax.w_xaxis.set_pane_color(white)
    ax.w_yaxis.set_pane_color(white)
    # Keep z pane

    # Get rid of the lines in 3d
    ax.w_xaxis.line.set_color(white)
    ax.w_yaxis.line.set_color(white)
    ax.w_zaxis.line.set_color(white)


def show2Dpose(channels, ax, lcolor="#3498db", rcolor="#e74c3c", add_labels=True):
  """
  Visualize a 2d skeleton

  Args
  channels: 64x1 vector. The pose to plot.
  ax: matplotlib axis to draw on
  lcolor: color for left part of the body
  rcolor: color for right part of the body
  add_labels: whether to add coordinate labels
  Returns
  Nothing. Draws on ax.
  """
  vals = np.reshape(channels, (-1, 2))

  # plt.plot(vals[:,0], vals[:,1], 'ro')
  I = np.array([0, 1, 2, 0, 4, 5, 0, 7, 8, 8, 10, 11, 8, 13, 14])  # start points
  J = np.array([1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15])  # end points
  LR = np.array([1, 1, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 1, 1], dtype=bool) # 1인 경우가 오른쪽

  # Make connection matrix
  for i in np.arange(len(I)):
    x, y = [np.array([vals[I[i], j], vals[J[i], j]]) for j in range(2)]

    ax.plot(x, -y, lw=2, c=lcolor if LR[i] else rcolor)

  # Get rid of the ticks
  #  ax.set_xticks([])
  #  ax.set_yticks([])
  #
  #  # Get rid of tick labels
  #  ax.get_xaxis().set_ticklabels([])
  #  ax.get_yaxis().set_ticklabels([])

  RADIUS = 1  # space around the subject
  xroot, yroot = vals[0, 0], vals[0, 1]
  #     ax.set_xlim([-RADIUS+xroot, RADIUS+xroot])
  #     ax.set_ylim([-RADIUS+yroot, RADIUS+yroot])

  ax.set_xlim([-1, 1])
  ax.set_ylim([-1, 1])

  if add_labels:
    ax.set_xlabel("x")
    ax.set_ylabel("-y")

  ax.set_aspect('equal')