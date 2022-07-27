def compute_precision_recall(det_performance_all, conf_thresh=0.5):

    if len(det_performance_all)==0 :
        print("no detections for conf_thresh = " + str(conf_thresh))
        return

    # extract the total number of positives, true positives, false negatives and false positives
    # format of det_performance_all is [ious, center_devs, pos_negs]
    pos_negs = []
    for item in det_performance_all:
        pos_negs.append(item[2])
    pos_negs_arr = np.asarray(pos_negs)        

    positives = sum(pos_negs_arr[:,0])
    true_positives = sum(pos_negs_arr[:,1])
    false_negatives = sum(pos_negs_arr[:,2])
    false_positives = sum(pos_negs_arr[:,3])
    print("TP = " + str(true_positives) + ", FP = " + str(false_positives) + ", FN = " + str(false_negatives))

    # compute precision
    precision = true_positives / (true_positives + false_positives) # When an object is detected, what are the chances of it being real?   

    # compute recall 
    recall = true_positives / (true_positives + false_negatives) # What are the chances of a real object being detected?

    print("precision = " + str(precision) + ", recall = " + str(recall) + ", conf_thres = " + str(conf_thresh) + "\n")    
