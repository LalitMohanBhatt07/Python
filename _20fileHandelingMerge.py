def merge_files():
    with open('myFile.txt','r') as file1:
        content1=file1.read()
        
        
    with open('intern.txt','r') as file2:
        content2=file2.read()
        
    merged_content=content1+content2
    with open('merge.txt','w') as merge_file:
        merge_file.write(merged_content)
        
        
merge_files()