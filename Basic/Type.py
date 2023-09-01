typeList=['Hello World',
          10,
          10.5,
          1j,
          [1,2],
          (1,2),
          range(3),
          {'name':'John'},
          {1,2},
          frozenset({"apple", "banana", "cherry"}),
          True,
          b'Hello',
          bytearray(5),
          memoryview(bytes(5)),
          None];

for var in typeList:
    print('The value of var is : ',var);
    print('The type of var is : ',type(var));
else:
    print('End. The length of list is : ',len(typeList));


