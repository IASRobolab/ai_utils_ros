available_detectors = []
pkg_name = "ai_utils_ros"

try:
    from ai_utils.detectors.Yolov8InferTrack import Yolov8InferTrack

    available_detectors.append("Yolov8InferTrack")
except ImportError:
    pass

try:
    from ai_utils.detectors.Yolov8Inference import Yolov8Inference

    available_detectors.append("Yolov8Inference")
except ImportError:
    pass

import rospy
import rospkg


class DetectorFactory:

    def __init__(self) -> None:

        score_threshold = rospy.get_param("~score_threshold", 0.6)
        return_image = rospy.get_param("~return_image", True)
        display_image = rospy.get_param("~display_image", False)

        detector = rospy.get_param("~detector", "")
        model_weights = rospy.get_param("~" + detector + "/model_weights", "")
        reid_weights = rospy.get_param("~" + detector + "/reid_weights", "")

        # Checks
        if detector == "":
            rospy.logerr("detector cannot be an empty string, available detectors are: " + available_detectors)
            exit(1)
        if detector in available_detectors:
            pass
        else:
            rospy.logerr("detector not found, available detectors are: " + ", ".join(available_detectors))
            exit(1)
        if model_weights == "":
            rospy.logerr("model_weights cannot be an empty string.")
            exit(1)

        self.detector = eval(detector)

        rospack = rospkg.RosPack()
        pkg_path = rospack.get_path(pkg_name)

        model_weights = pkg_path + "/weights/" + model_weights
        reid_weights = pkg_path + "/weights/" + reid_weights

        if reid_weights == "":
            self.detector = self.detector(model_weights, return_image, display_image, score_threshold)
        else:
            self.detector = self.detector(model_weights, reid_weights, return_image, display_image, score_threshold)

    @property
    def get_detector(self):
        return self.detector
