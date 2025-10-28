# test-api.ps1
# Simple test script for /product CRUD API

$baseUrl = "http://localhost:5000"

Write-Host "=== GET all products ==="
Invoke-RestMethod -Uri "$baseUrl/product" -Method GET | ConvertTo-Json -Depth 5
Write-Host ""

Write-Host "=== POST create a new product ==="
$body = @{
    name = "Test Product"
    price = 49.99
    stock = 10
    description = "A demo product for testing"
} | ConvertTo-Json

$newProduct = Invoke-RestMethod -Uri "$baseUrl/product" -Method POST -Body $body -ContentType "application/json"
$newProduct | ConvertTo-Json -Depth 5
$id = $newProduct.id
Write-Host ""

Write-Host "=== GET product by ID ==="
Invoke-RestMethod -Uri "$baseUrl/product/$id" -Method GET | ConvertTo-Json -Depth 5
Write-Host ""

Write-Host "=== PUT update product ==="
$updateBody = @{
    name = "Updated Product Name"
    price = 59.99
    stock = 8
} | ConvertTo-Json

Invoke-RestMethod -Uri "$baseUrl/product/$id" -Method PUT -Body $updateBody -ContentType "application/json" | ConvertTo-Json -Depth 5
Write-Host ""

Write-Host "=== DELETE product ==="
Invoke-RestMethod -Uri "$baseUrl/product/$id" -Method DELETE
Write-Host ""

Write-Host "=== GET all products after delete ==="
Invoke-RestMethod -Uri "$baseUrl/product" -Method GET | ConvertTo-Json -Depth 5
