'''
# sort() — altera a lista original
status_codes = [500, 200, 404, 201, 400]
print(status_codes)
status_codes.sort()
print(status_codes) # [200, 201, 400, 404, 500]


status_codes.sort(reverse=True)
print(status_codes) # [500, 404, 400, 201, 200]
'''
'''
# sorted() — retorna uma NOVA lista (original intacta)
endpoints = ["/usuarios", "/login", "/produtos", "/logout"]
print(sorted(endpoints)) # ['/login', '/logout', '/produtos', '/usuarios']


print(endpoints) # ['/usuarios', '/login', '/produtos', '/logout'] ← intacta
'''
