readinglist = ["But What Are You Really?", "Feminist Perspectives on the Self", "The Impossibility of Moral Responsibility", "In Defence of Free Will", "Philosophical Perspectives on the Insanity Defense", "Against Narrativity", "Not Passion’s Slave Robert C. Solomon", "Escapism and Self-Deception", "The Insanity Defense", "Hindu and Buddhist concepts of the self"]

names = ['Andrew Lee', 'Borna Navab', 'Ryan Magnuson Dickey', 'Samuel Engvall', 'Shankar Choudhury', 'Omara Esteghlal', 'James Kellogg', 'Hannah Judge', 'Zeos Greene']
x = 0
for i in readinglist:
    if x == len(names):
        x = 0
    print(i, names[x])
    x += 1
