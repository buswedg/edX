def azureml_main(frame1):
    sqrList = ["Relative Compactness", "Surface Area", "Wall Area"]
    sqredList = ["Relative Compactness Sqred", "Surface Area Sqred", "Wall Area Sqred"]
    frame1[sqredList] = frame1[sqrList]**2
    cubeList = ["Relative Compactness 3", "Surface Area 3", "Wall Area 3"]
    frame1[cubeList] = frame1[sqrList]**3
    return frame1
