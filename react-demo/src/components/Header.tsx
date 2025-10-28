interface HeaderProps {
  className?: string; // optional
}


export default function Header({className}: HeaderProps) {
  return (
    <header className={className ?? "layout-header"}>
      <h1>My App</h1>
      <nav>
        <a href="/">Home</a>
        <a href="/products">Products</a>
      </nav>
    </header>
  );
}