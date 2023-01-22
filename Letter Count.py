def Letter_Count():
    prompt='Please enter a word:\n'
    word=input(prompt)
    count=0
    prompt='Please enter a letter to count:\n'
    letters=input(prompt)
    for letter in word:
        if letter==letters:
            count=count+1
    print("Number of",letters,"'s in",word,':',count)
    prompt='Would you like to exit?\n'
    restart=input(prompt)
    if (restart=='Yes' or restart=='yes'):
        exit
    if (restart=='No' or restart=='no'):
        Letter_Count()
    else:
        exit
Letter_Count()       

    

