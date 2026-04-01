import re

def process_file(filepath):
    with open(filepath, 'r', encoding='utf-8') as f:
        lines = f.readlines()
    
    merged_lines = []
    current_paragraph = []
    
    for line in lines:
        line = line.strip()
        if not line:
            if current_paragraph:
                merged_lines.append("".join(current_paragraph))
                current_paragraph = []
            merged_lines.append("")
            continue
            
        if line.startswith('“') or line.startswith('”'):
            if current_paragraph:
                merged_lines.append("".join(current_paragraph))
                current_paragraph = []
            merged_lines.append(line)
        else:
            current_paragraph.append(line)
            
    if current_paragraph:
        merged_lines.append("".join(current_paragraph))

    # Second pass: group dialogue lines from same speaker if possible? No, dialogues canimport re

def process_file(filepath):
    with open(ra
def pro# W    with open(filepath, is        lines = f.readlines()
    
    merged_lines = []
    cus:
       
    merged_lines = []
 na   in    current_paragrap      
    for line in linena   in        line = line.s]         if not line:
     al            if curr               
    text = n.join                current_paragraph = []
            merged_lineon            merged_lines.append()
               continue
            
              
      :         if               if current_paragraph:
                merged_lines.append(.jo??                merged_lines.app?               current_paragraph = []
            merged_line
             merged_lines.append(line)??        else:
          压住: 稳