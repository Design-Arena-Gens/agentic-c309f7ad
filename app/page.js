'use client';

export default function Home() {
  return (
    <div style={{
      minHeight: '100vh',
      display: 'flex',
      flexDirection: 'column',
      alignItems: 'center',
      justifyContent: 'center',
      padding: '20px',
      backgroundColor: '#f5f5f5',
      fontFamily: 'Arial, sans-serif'
    }}>
      <div style={{
        backgroundColor: 'white',
        padding: '40px',
        borderRadius: '10px',
        boxShadow: '0 4px 6px rgba(0,0,0,0.1)',
        maxWidth: '800px',
        textAlign: 'center'
      }}>
        <h1 style={{
          color: '#0066cc',
          fontSize: '2.5em',
          marginBottom: '20px'
        }}>
          PHP Programming Tasks
        </h1>

        <p style={{
          fontSize: '1.2em',
          color: '#333',
          marginBottom: '30px'
        }}>
          Laboratory Report - Two PHP Programming Exercises
        </p>

        <div style={{
          backgroundColor: '#f0f8ff',
          padding: '20px',
          borderRadius: '8px',
          marginBottom: '30px',
          textAlign: 'left'
        }}>
          <h2 style={{ color: '#0066cc', fontSize: '1.5em', marginBottom: '15px' }}>Tasks Included:</h2>
          <ul style={{ fontSize: '1.1em', lineHeight: '1.8', color: '#333' }}>
            <li><strong>Task 1:</strong> Find the largest of three numbers using nested if statements</li>
            <li><strong>Task 2:</strong> Reverse a string using strrev() function</li>
          </ul>
        </div>

        <div style={{
          backgroundColor: '#fff3cd',
          padding: '15px',
          borderRadius: '8px',
          marginBottom: '30px',
          border: '2px solid #ffc107'
        }}>
          <p style={{ margin: 0, fontSize: '1.1em', color: '#856404' }}>
            📄 Each task includes: Aim, Problem Statement, Constraints, Procedure, Program, Output, and Conclusion
          </p>
        </div>

        <a
          href="/PHP_Programming_Tasks.pdf"
          download
          style={{
            display: 'inline-block',
            backgroundColor: '#0066cc',
            color: 'white',
            padding: '15px 40px',
            fontSize: '1.2em',
            textDecoration: 'none',
            borderRadius: '5px',
            fontWeight: 'bold',
            transition: 'background-color 0.3s'
          }}
          onMouseOver={(e) => e.target.style.backgroundColor = '#0052a3'}
          onMouseOut={(e) => e.target.style.backgroundColor = '#0066cc'}
        >
          📥 Download PDF Report
        </a>

        <div style={{
          marginTop: '40px',
          padding: '20px',
          backgroundColor: '#e7f3ff',
          borderRadius: '8px'
        }}>
          <h3 style={{ color: '#0066cc', marginBottom: '15px' }}>Program Outputs:</h3>

          <div style={{
            textAlign: 'left',
            backgroundColor: '#1e1e1e',
            color: '#d4d4d4',
            padding: '15px',
            borderRadius: '5px',
            marginBottom: '20px',
            fontFamily: 'Courier New, monospace',
            fontSize: '0.9em'
          }}>
            <strong style={{ color: '#4ec9b0' }}>Task 1 Output:</strong>
            <pre style={{ margin: '10px 0 0 0', whiteSpace: 'pre-wrap' }}>
{`=== Task 1: Find Largest of Three Numbers ===

Number 1: 45
Number 2: 78
Number 3: 62

The largest number is: 78`}
            </pre>
          </div>

          <div style={{
            textAlign: 'left',
            backgroundColor: '#1e1e1e',
            color: '#d4d4d4',
            padding: '15px',
            borderRadius: '5px',
            fontFamily: 'Courier New, monospace',
            fontSize: '0.9em'
          }}>
            <strong style={{ color: '#4ec9b0' }}>Task 2 Output:</strong>
            <pre style={{ margin: '10px 0 0 0', whiteSpace: 'pre-wrap' }}>
{`=== Task 2: Reverse a String ===

Original String: Hello World
Reversed String: dlroW olleH`}
            </pre>
          </div>
        </div>

        <footer style={{
          marginTop: '30px',
          paddingTop: '20px',
          borderTop: '1px solid #ddd',
          color: '#666',
          fontSize: '0.9em'
        }}>
          Generated on November 5, 2025
        </footer>
      </div>
    </div>
  );
}
