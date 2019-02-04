f = open("Q3a_processed.txt", "r")
openblock = False
blockline = 0
acc_lst = []
loss_lst = []
params = []
for x in f:
  if (x.startswith("##########") and openblock == False):
    openblock = True
    blockline = 0
    continue
  if (x.startswith("##########") and openblock == True):
    openblock = False
    # print (acc)
    # print(loss)
    continue
  if (openblock):
    blockline += 1
    if (blockline == 1):
      params.append(x)
    if (blockline == 3):
      acc = float(x.split()[1])
      # print(acc)
      acc_lst.append(acc)
    if (blockline == 4):
      loss = float(x.split()[2])
      # print(loss)
      loss_lst.append(loss)
print('Index: ',acc_lst.index(max(acc_lst)),' Max Accuracy: ',max(acc_lst))
print('Index: ',loss_lst.index(min(loss_lst)),' Minimum Loss: ',min(loss_lst))
print(params[acc_lst.index(max(acc_lst))])

