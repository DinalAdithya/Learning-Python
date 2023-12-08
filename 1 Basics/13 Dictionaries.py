# key need to be unique

weekly_conversions = {
    "mon":"monday",
    "tues":"tuesday",
    "wed":"wednessday",
    "thu":"thursday",
    "fri":"friday",
    "sat":"satterday",
    "sun":"sunday"
}

print(weekly_conversions["sun"]+"\n")

print(weekly_conversions.get("mon"))
print(weekly_conversions.get("gue"))
print(weekly_conversions.get("luv", "not valid key"))
