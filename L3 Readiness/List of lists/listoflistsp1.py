#treasure hunt game for list of lists

def main():
    tmap=[]

    for i in range(10):
        row=["X","X","X","X","X","X","X","X","X","X"]
        tmap.append(row)

    print("Here is your treasure map")
    for r in tmap:
        print(r)

if __name__ == "__main__":
    main()