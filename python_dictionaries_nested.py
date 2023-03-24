# словник може містити словники, що називається вкладеними словниками
myfamily = {
    "child1" : {
        "name" : "Emil",
        "year" : 2004
    },
    "child2" : {
        "name" : "Tobias",
        "year" : 2007
    },
    "child3" : {
        "name": "Linus",
        "year": 2011
    }
}
print(myfamily)
# або якщо ви хочете додати три словники в новий словник
child1 = {
    "name": "Emil",
    "year": 2004
}
child2 = {
    "name": "Tobias",
    "year": 2007
}
child3 = {
    "name": "Linus",
    "year": 2011
}
myfamily1 = {
    "child1": child1,
    "child2": child2,
    "child3": child3
}
print(myfamily1)
# щоб отримати доступ до елементів із вкладеного словника, ви викорстоуєте
# назву словників, починаючи із зовнішього блоку
print(myfamily["child2"]["name"])