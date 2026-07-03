Practical 3: PageRank for Link Analysis using Python
pages = {
    "Page 1":["Page 2","Page 3"],
    "Page 2":["Page 3"],
    "Page 3":["Page 1"],
    "Page 4":["Page 3"]
}

rank = {p:1 for p in pages}

for i in range(5):
    new = {p:0.15 for p in pages}
    for p in pages:
        for link in pages[p]:
            new[link] += 0.85*rank[p]/len(pages[p])
    rank = new

for page, value in rank.items():
    print(page, "=", round(value,2))
