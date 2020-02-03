#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# */AIPND-revision/intropyproject-classify-pet-images/get_pet_labels.py
#                                                                             
# PROGRAMMER: 
# DATE CREATED:                                  
# REVISED DATE: 
# PURPOSE: Create the function get_pet_labels that creates the pet labels from 
#          the image's filename. This function inputs: 
#           - The Image Folder as image_dir within get_pet_labels function and 
#             as in_arg.dir for the function call within the main function. 
#          This function creates and returns the results dictionary as results_dic
#          within get_pet_labels function and as results within main. 
#          The results_dic dictionary has a 'key' that's the image filename and
#          a 'value' that's a list. This list will contain the following item
#          at index 0 : pet image label (string).
#
##
# Imports python modules
from os import listdir


# TODO 2: Define get_pet_labels function below please be certain to replace None
#       in the return statement with results_dic dictionary that you create 
#       with this function
# 
def get_pet_labels(image_dir):
    """
    Creates a dictionary of pet labels (results_dic) based upon the filenames 
    of the image files. These pet image labels are used to check the accuracy 
    of the labels that are returned by the classifier function, since the 
    filenames of the images contain the true identity of the pet in the image.
    Be sure to format the pet labels so that they are in all lower case letters
    and with leading and trailing whitespace characters stripped from them.
    (ex. filename = 'Boston_terrier_02259.jpg' Pet label = 'boston terrier')
    Parameters:
     image_dir - The (full) path to the folder of images that are to be
                 classified by the classifier function (string)
    Returns:
      results_dic - Dictionary with 'key' as image filename and 'value' as a 
      List. The list contains for following item:
         index 0 = pet image label (string)
    """

    filename_list = listdir(image_dir)

    print("\nPrints 10 filenames from folder {}".format(image_dir))

    top_of_range = 10
    if len(filename_list) > 10:
        top_of_range = 10
    else:
        top_of_range = len(filename_list)

    for idx in range(0, top_of_range, 1):
        print('{:2d} file: {:>25}'.format(idx + 1, filename_list[idx]))

    results_dic = dict()

    items_in_dic = len(results_dic)
    print('\nEmtpy Dictionary results_dic - n items={}'.format(items_in_dic))

    pet_labels = []
    for idx in range(0, len(filename_list)):

        pet_image = filename_list[idx]

        low_pet_image = pet_image.lower()

        word_list_pet_image = low_pet_image.split('_')

        pet_name = ""

        for word in word_list_pet_image:
            if word.isalpha():
                pet_name += word + " "

        if (filename_list[idx]) not in results_dic:
            results_dic[filename_list[idx]] = [pet_name.strip()]
        else:
            print('** Warning: Key={} already exists in results_doc with value {}'.format(filename_list[idx], results_dic[filename_list[idx]]))

    print("\nPrinting all key-values pairs in dictionary resulst_doc:")
    for key in results_dic:
        print("Filename={}, Pet Label={}".format(key, results_dic[key][0]))

    # Replace None with the results_dic dictionary that you created with this
    # function
    return results_dic
