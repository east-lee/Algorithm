def main():
    word1, word2 = list(input() for _ in range(2))
    lcs = list([0]*(len(word1)+1) for _ in range(len(word2)+1))

    for i in range(1,len(word2)+1):
        for j in range(1,len(word1)+1):
            if word2[i-1] == word1[j-1]:
                lcs[i][j] = lcs[i-1][j-1]+1
            else:
                lcs[i][j] = max(lcs[i-1][j],lcs[i][j-1])
    print(lcs[-1][-1])



if __name__ == "__main__":
    main()