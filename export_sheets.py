import json
import openpyxl
from openpyxl.styles import Font, PatternFill, Alignment, Border, Side
from openpyxl.utils import get_column_letter

# Load data
with open('mendix_advanced_unique_314.json', encoding='utf-8') as f:
    u314 = json.load(f)

with open('mendix_advanced_data.json', encoding='utf-8') as f:
    exams_data = json.load(f)

wb = openpyxl.Workbook()
# Remove default sheet
wb.remove(wb.active)

# Styles
header_font = Font(name='Segoe UI', size=11, bold=True, color='FFFFFF')
header_fill = PatternFill(start_color='1F4E79', end_color='1F4E79', fill_type='solid')
header_align = Alignment(horizontal='center', vertical='center', wrap_text=True)

cell_font = Font(name='Segoe UI', size=10)
cell_align_left = Alignment(horizontal='left', vertical='top', wrap_text=True)
cell_align_center = Alignment(horizontal='center', vertical='top')

thin_border = Border(
    left=Side(style='thin', color='D9D9D9'),
    right=Side(style='thin', color='D9D9D9'),
    top=Side(style='thin', color='D9D9D9'),
    bottom=Side(style='thin', color='D9D9D9')
)

headers = [
    'ID', 'Chủ đề (Topic)', 'Đề thi xuất hiện', 'Câu hỏi (Question)',
    'Đáp án A', 'Đáp án B', 'Đáp án C', 'Đáp án D', 'Đáp án E', 'Đáp án F',
    'Đáp án đúng', 'Giải thích chi tiết (Explanation)'
]

col_widths = {
    1: 8,    # ID
    2: 22,   # Topic
    3: 25,   # Exams
    4: 55,   # Question
    5: 35,   # Opt A
    6: 35,   # Opt B
    7: 35,   # Opt C
    8: 35,   # Opt D
    9: 25,   # Opt E
    10: 25,  # Opt F
    11: 15,  # Correct Ans
    12: 60   # Explanation
}

exam_names = {
    '1': 'Đề 1 (50 câu)',
    '2': 'Đề 2 (50 câu)',
    '3': 'Đề 3 (50 câu)',
    'new_practice_test_1': 'Practice Test I (50 câu)',
    'new_practice_set_1': 'Practice Questions Set 1 (30 câu)',
    'new_practice_set_2': 'Practice Questions Set 2 (30 câu)',
    'new_learning_path': 'Learning Path Quiz Bank (150 câu)'
}

def format_exam_tags(appeared):
    tags = []
    for item in appeared:
        s = str(item)
        tags.append(exam_names.get(s, f"Đề {s}"))
    return ", ".join(tags)

def create_sheet(title, questions_list):
    ws = wb.create_sheet(title=title)
    ws.views.sheetView[0].showGridLines = True
    ws.freeze_panes = 'A2'
    ws.row_dimensions[1].height = 28
    
    # Write headers
    for col_idx, h in enumerate(headers, 1):
        cell = ws.cell(row=1, column=col_idx, value=h)
        cell.font = header_font
        cell.fill = header_fill
        cell.alignment = header_align
        cell.border = thin_border
        
    for row_idx, q in enumerate(questions_list, 2):
        ws.row_dimensions[row_idx].height = 35 # will expand as needed
        
        # Options map
        opts_map = {}
        for opt in q.get('opts', []):
            opts_map[opt.get('k', '')] = opt.get('t', '')
            
        ans_str = ", ".join(q.get('ans', []))
        appeared_str = format_exam_tags(q.get('appeared_in_exams', []))
        
        row_values = [
            q.get('id', row_idx - 1),
            q.get('topic', 'General'),
            appeared_str,
            q.get('q', ''),
            opts_map.get('A', ''),
            opts_map.get('B', ''),
            opts_map.get('C', ''),
            opts_map.get('D', ''),
            opts_map.get('E', ''),
            opts_map.get('F', ''),
            ans_str,
            q.get('exp', '')
        ]
        
        for col_idx, val in enumerate(row_values, 1):
            cell = ws.cell(row=row_idx, column=col_idx, value=val)
            cell.font = cell_font
            cell.border = thin_border
            if col_idx in [1, 11]:
                cell.alignment = cell_align_center
            else:
                cell.alignment = cell_align_left

    # Column widths
    for col_idx, w in col_widths.items():
        ws.column_dimensions[get_column_letter(col_idx)].width = w

# 1. Master sheet: 314 unique questions
print("Creating Master Sheet: Tong_Hop_314_Cau...")
create_sheet('Tong_Hop_314_Cau', u314)

# 2. Individual Exam sheets
sheet_map = [
    ('De_1_50_Cau', '1'),
    ('De_2_50_Cau', '2'),
    ('De_3_50_Cau', '3'),
    ('Practice_Test_I_50_Cau', 'new_practice_test_1'),
    ('Practice_Set_1_30_Cau', 'new_practice_set_1'),
    ('Practice_Set_2_30_Cau', 'new_practice_set_2'),
    ('Learning_Path_150_Cau', 'new_learning_path')
]

for sheet_title, exam_key in sheet_map:
    print(f"Creating sheet: {sheet_title}...")
    q_list = exams_data.get(exam_key, [])
    # Add appeared_in_exams if not present
    for q in q_list:
        if 'appeared_in_exams' not in q:
            q['appeared_in_exams'] = [exam_key]
    create_sheet(sheet_title, q_list)

xlsx_path = 'De_Mendix_Advanced_314_Cau_Hoi.xlsx'
wb.save(xlsx_path)
print(f"Successfully saved {xlsx_path}!")

# Export CSV for master sheet
import csv

csv_path = 'De_Mendix_Tong_Hop_314_Cau.csv'
with open(csv_path, 'w', encoding='utf-8-sig', newline='') as f:
    writer = csv.writer(f)
    writer.writerow(headers)
    for q in u314:
        opts_map = {opt.get('k', ''): opt.get('t', '') for opt in q.get('opts', [])}
        writer.writerow([
            q.get('id', ''),
            q.get('topic', 'General'),
            format_exam_tags(q.get('appeared_in_exams', [])),
            q.get('q', ''),
            opts_map.get('A', ''),
            opts_map.get('B', ''),
            opts_map.get('C', ''),
            opts_map.get('D', ''),
            opts_map.get('E', ''),
            opts_map.get('F', ''),
            ", ".join(q.get('ans', [])),
            q.get('exp', '')
        ])

print(f"Successfully saved {csv_path}!")
