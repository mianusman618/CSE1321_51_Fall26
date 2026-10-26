states = ["Georgia", "Florida", "Alabama", "Tennessee", "S. Carolina"]
for i in range(len(states)):
    print(states[i])
    if "e" in states[i]:
        print("This state contains letter e")
        states[i]="Texas"
print(states)
