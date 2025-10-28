import { useEffect, useState } from "react";
import Layout from "../components/Layout";
import type { Product } from "../types/types";
import "./Products.css";

export default function ProductsPage() {
  const [products, setProducts] = useState<Product[]>([]);
  const [loading, setLoading] = useState(true);
  const [error, setError] = useState<string | null>(null);

  const API_URL = "http://localhost:5000/api/product";

  // Fetch products
  const fetchProducts = async () => {
    setLoading(true);
    try {
      const res = await fetch(API_URL);
      if (!res.ok) throw new Error(`HTTP error: ${res.status}`);
      const data: Product[] = await res.json();
      setProducts(data);
    } catch (err: any) {
      setError(err.message);
    } finally {
      setLoading(false);
    }
  };

  useEffect(() => {
    fetchProducts();
  }, []);

  // Delete product
  const deleteProduct = async (id: number) => {
    try {
      const res = await fetch(`${API_URL}/${id}`, { method: "DELETE" });
      if (!res.ok) throw new Error(`Failed to delete: ${res.status}`);
      setProducts(products.filter(p => p.id !== id));
    } catch (err: any) {
      alert(err.message);
    }
  };

  // Create product
  const createProduct = async () => {
    const name = prompt("Enter product name:");
    if (!name) return;

    const priceStr = prompt("Enter price:") || "0";
    const price = parseFloat(priceStr);

    const stockStr = prompt("Enter stock quantity:") || "0";
    const stock = parseInt(stockStr);

    const description = prompt("Enter description:") || "";

    const newProduct = { name, price, stock, description };

    try {
      const res = await fetch(API_URL, {
        method: "POST",
        headers: { "Content-Type": "application/json" },
        body: JSON.stringify(newProduct),
      });
      if (!res.ok) throw new Error(`Failed to create: ${res.status}`);
      const created: Product = await res.json();
      setProducts([...products, created]);
    } catch (err: any) {
      alert(err.message);
    }
  };

  // Update product
  const updateProduct = async (product: Product) => {
    const name = prompt("New name:", product.name);
    if (!name) return;

    const priceStr = prompt("New price:", product.price.toString()) || "0";
    const price = parseFloat(priceStr);

    const stockStr = prompt("New stock:", product.stock.toString()) || "0";
    const stock = parseInt(stockStr);

    const description = prompt("Enter description:") || "";

    const updatedProduct = { ...product, name, price, stock, description };

    try {
      const res = await fetch(`${API_URL}/${product.id}`, {
        method: "PUT",
        headers: { "Content-Type": "application/json" },
        body: JSON.stringify(updatedProduct),
      });
      if (!res.ok) throw new Error(`Failed to update: ${res.status}`);
      const updated: Product = await res.json();
      setProducts(products.map(p => (p.id === updated.id ? updated : p)));
    } catch (err: any) {
      alert(err.message);
    }
  };

  return (
    <Layout>
      <h2>Products</h2>
      <button className="button button-create" onClick={createProduct}>Create New Product</button>

      {loading && <p>Loading...</p>}
      {error && <p style={{ color: "red" }}>{error}</p>}

      <div className="products-grid">
        {products.map((p) => (
          <div key={p.id} className="product-card">
            <h3>{p.name}</h3>
            <p><strong>Price:</strong> ${p.price}</p>
            <p><strong>Stock:</strong> {p.stock}</p>
            <p>{p.description}</p>
            <div className="product-buttons">
              <button className="button button-update" onClick={() => updateProduct(p)}>Update</button>
              <button className="button button-delete" onClick={() => deleteProduct(p.id)}>Delete</button>
            </div>
          </div>
        ))}
      </div>

    </Layout>
  );
}
