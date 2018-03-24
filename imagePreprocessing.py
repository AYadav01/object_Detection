#This function preprocesses extracted images and removes any unsupported/blank images

def find_bad():
    for file_type in ['neg']:

        #start iterating throught all the images in bad_neg_pic
        for img in os.listdir(file_type):
            for bad in os.listdir('bad_neg_pic'):
                try:

                    #file_type is directory path
                    current_image_path = str(file_type) + '/' + str(img)
                    bad = cv2.imread('bad_neg_pic/' + str(bad))
                    
                    #grabs a sample bad images that we want to remove
                    question = cv2.imread(current_image_path)
                    
                    #bitwise_xor conditional is True if either one of the condition is met,
                    #if both of the conditions are met, then it becomes False
                    #if the image in 'bad_neg_pic' folder has same shape and property as the image  
                    #extracted images in 'neg' folder, it is then removed
                    if bad.shape == question.shape and not(np.bitwise_xor(bad, question).any()):
                        print('Found one!')
                        print(current_image_path)

                        #if we find the 'bad' image, we remove it
                        os.remove(current_image_path)
                
                except Exception as e:
                    print(str(e))
    print('Done all!')

if __name__ == '__main__':
	find_bad()