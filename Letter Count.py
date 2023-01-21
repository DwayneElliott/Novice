def Letter_Count():
    prompt='Please enter a word.\n'
    word=input(prompt)
    count=0
    prompt1='Please enter letter to count\n'
    letters=input(prompt1)
    for letter in word:
        if letter==letters:
            count=count+1
    print("Number of letters's in",word,':',count)
    prompt2='Would you like to exit?\n'
    restart=input(prompt2)
    if (restart=='Yes' or restart=='yes'):
        exit
    if (restart=='No' or restart=='no'):
        Letter_Count()
    else:
        exit
Letter_Count()    

    

