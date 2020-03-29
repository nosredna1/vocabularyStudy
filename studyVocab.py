# -*- coding: utf-8 -*-
"""
Created on Sat Feb 29 19:22:23 2020

@author: duong
"""

def readWorksheet(name):
    import pandas as pd
    
    xlsx = pd.ExcelFile(name)
    df = pd.read_excel(xlsx)

    return df

def obtainLesson(df):
    lessonNo = input('Enter Lesson Number: ')
    lessonNoLower_str = 'Lesson ' + lessonNo
    
    lessonNoUpper = int(lessonNo) + 1
    lessonNoUpper_str = 'Lesson ' + str(lessonNoUpper)
    
    unfiltered_data = df[[1, 2]]

    indexUpper = unfiltered_data[unfiltered_data[1] == \
                                  lessonNoUpper_str].index.tolist()
    indexLower = unfiltered_data[unfiltered_data[1] ==\
                                  lessonNoLower_str].index.tolist()
    
    try: 
        specifiedLesson = unfiltered_data.loc[indexLower[0] + 1:indexUpper[0] - 1]
    except:
        specifiedLesson = unfiltered_data.loc[indexLower[0] + 1:]
    
    return specifiedLesson

def randomizedVocab(nonRandomized):
    # Pandas sample function to randomize vocabulary
    randomized = nonRandomized.sample(frac=1).reset_index(drop=True)
    
    return randomized

def continuousStudy(vocabulary):
    rowCount = len(vocabulary.index)
    
    # Row Count
    indexCount = 0
    # Keep iterating until all vocabulary is correctly answered
    while rowCount > 0:
        foreign = vocabulary.iloc[indexCount][1] # Column 1
        english = vocabulary.iloc[indexCount][2] # Column 2
        
        answer = input(foreign + ': ')
        if answer.upper() == 'STOP':
            rowCount = 0
            break
            
        # User inputs if answer is correct
        correctYN = input('Answer is \'' + english + '\'.\n' 
                          + 'Was your answer correct? (Y/N): ')     
        
        if correctYN.upper() == 'Y':
            vocabulary = vocabulary.drop(index = indexCount).reset_index(drop=True)
            rowCount = len(vocabulary.index)
        else:
            indexCount+=1        
    
        if indexCount == rowCount:
            indexCount = 0

if __name__ == "__main__":
    
    worksheetName = 'vietnamese vocabulary.xlsx'
    
    sheet = readWorksheet(worksheetName)
    vocabulary = obtainLesson(sheet)
    
    randomizedStudy = randomizedVocab(vocabulary)
    continuousStudy(randomizedStudy)