import numpy as np
def calculate_iou(gt_mask, fg_mask):
    """
    Calculate the intersection over union (IoU) of a ground truth mask and a foreground mask.
    :param gt_mask: A numpy array representing the ground truth mask.
    :param fg_mask: A numpy array representing the foreground mask.
    :return: The IoU between the two masks.
    """
    intersection = np.logical_and(gt_mask, fg_mask)
    union = np.logical_or(gt_mask, fg_mask)
    iou = np.sum(intersection) / np.sum(union)
    return iou