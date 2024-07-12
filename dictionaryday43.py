bill={'january':250,
      'february':300,
      'march':140,
      'april':210,
      'may':110,
      'june':120,
      'july':130,
      'august':230,
      'september':180,
      'october':190,
      'november':260,
      'december':145

}
total=sum(bill.values())
print(f"total bill is{total}")
print(f"avg bill is{total/12}")