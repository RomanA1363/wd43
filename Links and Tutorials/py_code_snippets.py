# basic loop
for i in range (6):
    print (i)



ax = df['medication'].value_counts() \
.head(10) \
.plot(kind = 'bar', title = 'Just a title')
ax.set_xlabel('Medicine')
ax.set_ylabel('Rx')



#for i in range (1):

#   p=xPatient (
#         str(uuid.uuid4()),
#         fake.last_name(),
#         fake.ssn(),
#         random.randint(10, 99),
#         address = Address(
#            fake.street_address(),
#            fake.city(),
#            random.choice(us_states),
#            fake.postcode(),
#            [
#               random.randint(1, 1000),
#               random.randint(1, 1000)
#             ]
#                          )
#    )
#   j=json.dumps(dataclasses.asdict(p), indent=4)
#   print(j)

# print(test(10))

