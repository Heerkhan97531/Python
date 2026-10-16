print("====Unique Website Visitor & Interest Tracker=====")

insta_visitors = {"laiba", "noor", "ali", "ayra", "heer"}
linkedIn_visitor ={"ayra", "ali", "manat", "huraira", "hussain"}
print(insta_visitors)
print(linkedIn_visitor)
# insta_visitors.count("laiba")
print(len(linkedIn_visitor))
combined = insta_visitors.union(linkedIn_visitor)
print("the total visitors of insta and LinkedIn are these: ",combined)

findout = insta_visitors.intersection(linkedIn_visitor)
print("these are the visitors who have to visit both instagram and linkedIn profile:",findout)


if insta_visitors:
    pulled_out = insta_visitors.difference(findout)
    print("they just have to visit instagram, they don't visit linkedin: ", pulled_out)

