import array as arr
arr1 = arr.array('i', range(256))
arr2 = arr.array('i', arr1)

keyStr = input("Enter the key: ")
while(len(keyStr) > 256):
    print("Key size can not be greater than 256")
    keyStr = input("Enter the key: ")

keyArr = arr.array('i', range(len(keyStr)))
for i in range(len(keyStr)):
    keyArr[i] = ord(keyStr[i])

temp = arr.array('i', range(256))
for i in range(256):
    temp[i] = keyArr[i % len(keyArr)]

j = 0
for i in range(256):
    j = (j + arr2[i] + temp[i]) % 256
    var = arr2[i]
    arr2[i] = arr2[j]
    arr2[j] = var

# print(arr1)
print(arr2)
print(keyStr)
print(keyArr)
print(temp)
