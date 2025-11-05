#!/usr/bin/env python3
from reportlab.lib.pagesizes import letter, A4
from reportlab.platypus import SimpleDocTemplate, Paragraph, Spacer, PageBreak, Image, Table, TableStyle, Preformatted
from reportlab.lib.styles import getSampleStyleSheet, ParagraphStyle
from reportlab.lib.units import inch
from reportlab.lib.enums import TA_CENTER, TA_LEFT, TA_JUSTIFY
from reportlab.lib import colors

# Create PDF
pdf_filename = "PHP_Programming_Tasks.pdf"
doc = SimpleDocTemplate(pdf_filename, pagesize=letter,
                        rightMargin=72, leftMargin=72,
                        topMargin=72, bottomMargin=18)

# Container for the 'Flowable' objects
elements = []

# Define styles
styles = getSampleStyleSheet()
styles.add(ParagraphStyle(name='CenterTitle', alignment=TA_CENTER, fontSize=24, spaceAfter=30, textColor=colors.HexColor('#1a1a1a'), fontName='Helvetica-Bold'))
styles.add(ParagraphStyle(name='SubTitleStyle', alignment=TA_CENTER, fontSize=16, spaceAfter=20, textColor=colors.HexColor('#333333')))
styles.add(ParagraphStyle(name='TaskTitle', fontSize=18, spaceAfter=12, textColor=colors.HexColor('#0066cc'), fontName='Helvetica-Bold'))
styles.add(ParagraphStyle(name='SectionTitle', fontSize=14, spaceAfter=10, textColor=colors.HexColor('#0066cc'), fontName='Helvetica-Bold'))
styles.add(ParagraphStyle(name='BodyTextStyle', fontSize=11, spaceAfter=12, alignment=TA_JUSTIFY))
styles.add(ParagraphStyle(name='CodeStyle', fontSize=9, fontName='Courier', leftIndent=20, rightIndent=20, spaceAfter=12, backColor=colors.HexColor('#f5f5f5')))

# Front Page
elements.append(Spacer(1, 2*inch))
elements.append(Paragraph("PHP PROGRAMMING", styles['CenterTitle']))
elements.append(Paragraph("LABORATORY TASKS", styles['CenterTitle']))
elements.append(Spacer(1, 0.5*inch))
elements.append(Paragraph("Submitted By: Student", styles['SubTitleStyle']))
elements.append(Spacer(1, 0.3*inch))
elements.append(Paragraph("Date: November 5, 2025", styles['SubTitleStyle']))
elements.append(PageBreak())

# Task 1
elements.append(Paragraph("TASK 1", styles['TaskTitle']))
elements.append(Spacer(1, 0.2*inch))

elements.append(Paragraph("AIM", styles['SectionTitle']))
elements.append(Paragraph("To write a PHP program to find the largest of three numbers using nested if statements.", styles['BodyTextStyle']))
elements.append(Spacer(1, 0.15*inch))

elements.append(Paragraph("PROBLEM STATEMENT", styles['SectionTitle']))
elements.append(Paragraph("Write a PHP program that accepts three numbers as input and determines which number is the largest using nested if-else statements.", styles['BodyTextStyle']))
elements.append(Spacer(1, 0.15*inch))

elements.append(Paragraph("CONSTRAINTS", styles['SectionTitle']))
elements.append(Paragraph("• Must use nested if statements<br/>• Must compare three numbers<br/>• Should handle equal values correctly", styles['BodyTextStyle']))
elements.append(Spacer(1, 0.15*inch))

elements.append(Paragraph("PROCEDURE", styles['SectionTitle']))
elements.append(Paragraph("1. Initialize three variables with numeric values<br/>2. Use the first if statement to compare num1 and num2<br/>3. Inside each branch, use nested if to compare with num3<br/>4. Assign the largest value to a variable<br/>5. Display the result", styles['BodyTextStyle']))
elements.append(Spacer(1, 0.15*inch))

elements.append(Paragraph("PROGRAM", styles['SectionTitle']))
code1 = """<?php
// Task 1: Find the largest of three numbers using nested if

echo "=== Task 1: Find Largest of Three Numbers ===\\n\\n";

// Input three numbers
$num1 = 45;
$num2 = 78;
$num3 = 62;

echo "Number 1: $num1\\n";
echo "Number 2: $num2\\n";
echo "Number 3: $num3\\n\\n";

// Find largest using nested if
if ($num1 >= $num2) {
    if ($num1 >= $num3) {
        $largest = $num1;
    } else {
        $largest = $num3;
    }
} else {
    if ($num2 >= $num3) {
        $largest = $num2;
    } else {
        $largest = $num3;
    }
}

echo "The largest number is: $largest\\n";
?>"""
elements.append(Preformatted(code1, styles['CodeStyle']))
elements.append(Spacer(1, 0.15*inch))

elements.append(Paragraph("OUTPUT", styles['SectionTitle']))
output1 = """=== Task 1: Find Largest of Three Numbers ===

Number 1: 45
Number 2: 78
Number 3: 62

The largest number is: 78"""
elements.append(Preformatted(output1, styles['CodeStyle']))
elements.append(Spacer(1, 0.15*inch))

elements.append(Paragraph("CONCLUSION", styles['SectionTitle']))
elements.append(Paragraph("The PHP program successfully determines the largest of three numbers using nested if statements. The program correctly compares the three numbers (45, 78, and 62) and identifies 78 as the largest number. The nested if structure provides a logical flow for comparing multiple values sequentially.", styles['BodyTextStyle']))

elements.append(PageBreak())

# Task 2
elements.append(Paragraph("TASK 2", styles['TaskTitle']))
elements.append(Spacer(1, 0.2*inch))

elements.append(Paragraph("AIM", styles['SectionTitle']))
elements.append(Paragraph("To write a PHP program to reverse a string using the strrev() function.", styles['BodyTextStyle']))
elements.append(Spacer(1, 0.15*inch))

elements.append(Paragraph("PROBLEM STATEMENT", styles['SectionTitle']))
elements.append(Paragraph("Write a PHP program that accepts a string as input and reverses it using the built-in strrev() function.", styles['BodyTextStyle']))
elements.append(Spacer(1, 0.15*inch))

elements.append(Paragraph("CONSTRAINTS", styles['SectionTitle']))
elements.append(Paragraph("• Must use the strrev() function<br/>• Should handle strings with spaces<br/>• Should preserve character case", styles['BodyTextStyle']))
elements.append(Spacer(1, 0.15*inch))

elements.append(Paragraph("PROCEDURE", styles['SectionTitle']))
elements.append(Paragraph("1. Initialize a string variable with a value<br/>2. Display the original string<br/>3. Use the strrev() function to reverse the string<br/>4. Store the reversed string in a new variable<br/>5. Display the reversed string", styles['BodyTextStyle']))
elements.append(Spacer(1, 0.15*inch))

elements.append(Paragraph("PROGRAM", styles['SectionTitle']))
code2 = """<?php
// Task 2: Reverse a string using strrev()

echo "=== Task 2: Reverse a String ===\\n\\n";

// Input string
$originalString = "Hello World";

echo "Original String: $originalString\\n";

// Reverse the string using strrev()
$reversedString = strrev($originalString);

echo "Reversed String: $reversedString\\n";
?>"""
elements.append(Preformatted(code2, styles['CodeStyle']))
elements.append(Spacer(1, 0.15*inch))

elements.append(Paragraph("OUTPUT", styles['SectionTitle']))
output2 = """=== Task 2: Reverse a String ===

Original String: Hello World
Reversed String: dlroW olleH"""
elements.append(Preformatted(output2, styles['CodeStyle']))
elements.append(Spacer(1, 0.15*inch))

elements.append(Paragraph("CONCLUSION", styles['SectionTitle']))
elements.append(Paragraph("The PHP program successfully reverses a string using the strrev() function. The program takes the input string 'Hello World' and produces the reversed output 'dlroW olleH'. The strrev() function is a built-in PHP function that efficiently reverses strings while preserving character case and special characters including spaces.", styles['BodyTextStyle']))

# Build PDF
doc.build(elements)

print(f"PDF generated successfully: {pdf_filename}")
