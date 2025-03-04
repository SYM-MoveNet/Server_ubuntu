
PART_NAMES = [
    "nose", "leftEye", "rightEye", "leftEar", "rightEar", "leftShoulder",
    "rightShoulder", "leftElbow", "rightElbow", "leftWrist", "rightWrist",
    "leftHip", "rightHip", "leftKnee", "rightKnee", "leftAnkle", "rightAnkle"
]

NUM_KEYPOINTS = len(PART_NAMES)

PART_IDS = {pn: pid for pid, pn in enumerate(PART_NAMES)}

CONNECTED_PART_NAMES = [
    ("leftHip", "leftShoulder"), ("leftElbow", "leftShoulder"),
    ("leftElbow", "leftWrist"), ("leftHip", "leftKnee"),
    ("leftKnee", "leftAnkle"), ("rightHip", "rightShoulder"),
    ("rightElbow", "rightShoulder"), ("rightElbow", "rightWrist"),
    ("rightHip", "rightKnee"), ("rightKnee", "rightAnkle"),
    ("leftShoulder", "rightShoulder"), ("leftHip", "rightHip")
]

CONNECTED_PART_INDICES = [(PART_IDS[a], PART_IDS[b]) for a, b in CONNECTED_PART_NAMES]

## ================================ 새로운 kpt를 위한 추가 ================================================
NEW_PART_NAMES = [
    "Hip", "rightHip", "rightKnee", "rightAnkle", "leftHip", "leftKnee",
    "leftAnkle", "Center", "shoulderCenter", "Eye", "leftShoulder",
    "leftElbow", "leftWrist", "rightShoulder", "rightElbow", "rightWrist"
]

NEW_PART_IDS = {pn: pid for pid, pn in enumerate(NEW_PART_NAMES)}

NEW_CONNECTED_PART_NAMES = [
    ("Hip", "rightHip"), ("Hip", "leftHip"),
    ("rightKnee", "rightHip"), ("rightAnkle", "rightKnee"),
    ("leftKnee", "leftHip"), ("leftAnkle", "leftKnee"),
    ("Center", "Hip"), ("shoulderCenter", "Center"),
    ("shoulderCenter", "rightShoulder"), ("rightElbow", "rightShoulder"),
    ("rightWrist", "rightElbow"), ("shoulderCenter", "leftShoulder"),
    ("leftShoulder", "leftElbow"), ("leftElbow", "leftWrist"), ("Eye", "shoulderCenter")
]

NEW_CONNECTED_PART_INDICES = [(NEW_PART_IDS[a], NEW_PART_IDS[b]) for a, b in NEW_CONNECTED_PART_NAMES]
## ==================================================================================================

LOCAL_MAXIMUM_RADIUS = 1

POSE_CHAIN = [
    ("nose", "leftEye"), ("leftEye", "leftEar"), ("nose", "rightEye"),
    ("rightEye", "rightEar"), ("nose", "leftShoulder"),
    ("leftShoulder", "leftElbow"), ("leftElbow", "leftWrist"),
    ("leftShoulder", "leftHip"), ("leftHip", "leftKnee"),
    ("leftKnee", "leftAnkle"), ("nose", "rightShoulder"),
    ("rightShoulder", "rightElbow"), ("rightElbow", "rightWrist"),
    ("rightShoulder", "rightHip"), ("rightHip", "rightKnee"),
    ("rightKnee", "rightAnkle")
]

PARENT_CHILD_TUPLES = [(PART_IDS[parent], PART_IDS[child]) for parent, child in POSE_CHAIN]

PART_CHANNELS = [
  'left_face',
  'right_face',
  'right_upper_leg_front',
  'right_lower_leg_back',
  'right_upper_leg_back',
  'left_lower_leg_front',
  'left_upper_leg_front',
  'left_upper_leg_back',
  'left_lower_leg_back',
  'right_feet',
  'right_lower_leg_front',
  'left_feet',
  'torso_front',
  'torso_back',
  'right_upper_arm_front',
  'right_upper_arm_back',
  'right_lower_arm_back',
  'left_lower_arm_front',
  'left_upper_arm_front',
  'left_upper_arm_back',
  'left_lower_arm_back',
  'right_hand',
  'right_lower_arm_front',
  'left_hand'
]