export const metadata = {
  title: 'PHP Programming Tasks',
  description: 'Laboratory report for PHP programming exercises',
}

export default function RootLayout({ children }) {
  return (
    <html lang="en">
      <body>{children}</body>
    </html>
  )
}
