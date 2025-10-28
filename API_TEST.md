# API TEST
## BASH
**GET All**
```
curl -X GET http://localhost:5000/product
```
**GET by id**
```
curl -X GET http://localhost:5000/product/1
```
**POST new product**
```
curl -X POST http://localhost:5000/product \
  -H "Content-Type: application/json" \
  -d '{
    "name": "Test Product"
  }'
```

**PUT update product**
```
curl -X PUT http://localhost:5000/product/1 \
  -H "Content-Type: application/json" \
  -d '{
    "name": "Updated Product Name"
  }'
```
**DELETE product**
```
curl -X DELETE http://localhost:5000/product/1
```

## Powershell
**GET All**
```
Invoke-RestMethod -Uri "http://localhost:5000/product" -Method GET
```
**GET by id**
```
Invoke-RestMethod -Uri "http://localhost:5000/product/1" -Method GET
```
**POST new product**
```
Invoke-RestMethod -Uri "http://localhost:5000/product" -Method POST -ContentType "application/json" -Body '{"name":"Test Product","price":49.99,"stock":10,"description":"A demo product for testing"}'
```

**PUT update product**
```
Invoke-RestMethod -Uri "http://localhost:5000/product/1" -Method PUT -ContentType "application/json" -Body '{"name":"Updated Product Name","price":59.99,"stock":8}'

```
**DELETE product**
```
Invoke-RestMethod -Uri "http://localhost:5000/product/1" -Method DELETE
``` 