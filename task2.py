print("\nSwallow Speed Analysis: Version 1.0\n")
results = []
while True: #To loop the code
    reading = input("Enter the next reading:")
    if reading==(""): #if reading is empty then it breaks the loop
        break
    elif (reading.lower()[0]!="u" and reading.lower()[0]!="e") or (reading[1:].isalpha()):
        print("Invalid Input")
        continue
    else:
        if reading.lower().startswith('e'): #it checks reading start from e or not
            results.append((float(reading[1:])/1.60934))
        else:
            results.append(float(reading[1:]))
        print("Reading Saved.")

if results == []: #it checks the list
    print("No Readings Found. Nothing to do.")
else:
    minimum = min(results)
    maximum = max(results)
    average=  sum(results)/len(results)

    print("\nResults Summary\n")
    print("\nReadings Analysed\n")
    print(f"Min speed: {minimum:.1f} MPH,{minimum*1.60934:.1f} KHP")
    print(f"Max speed: {maximum:.1f} MPH,{maximum*1.60934:.1f} KHP")
    print(f"Average speed: {average:.1f} MPH,{average*1.60934:.1f} KHP")