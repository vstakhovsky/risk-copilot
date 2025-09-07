
export default function RootLayout({ children }: { children: React.ReactNode }) {
  return (<html lang="en"><body style={{fontFamily:'Inter',padding:16}}>
    <nav style={{display:'flex',gap:12,marginBottom:16}}>
      <a href="/">Home</a><a href="/upload">Upload</a>
      <a href="/artifacts">Artifacts</a><a href="/status">Status</a><a href="/admin">Admin</a>
    </nav>{children}</body></html>);
}
