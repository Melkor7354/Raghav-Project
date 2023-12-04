player_base = [['LIONEL MESSI', 'RW', 90], ['CRISTIANO RONALDO', 'ST', 86],
               ['TONI KROOS', 'CM', 86], ['GARNACHO', 'LW', 75], ['HARRY KANE', 'ST', 90],
               ['SON', 'LW', 87], ['COLE PALMER', 'CAM', 66], ['STERLING', 'LW', 83],
               ['ENZO', 'CM', 83], ['JAMAL MUSIALA', 'CAM', 86], ['JUDE BELLINGHAM', 'CM', 86],
               ['JEREMY DOKU', 'RW', 77], ['MARCUS RAHSFORD', 'LW', 85], ['SOFYAN AMRABAT', 'CM', 80],
               ['RASMUS HOJLUND', 'ST', 76], ['PEDRI', 'CM', 86], ['PABLO GAVI', 'CB', 83],
               ['WILLIAM SALIBA', 'CB', 83], ['DAYOT UPAMECANO', 'CB', 82], ['KEVIN DE BRUYNE', 'CAM', 91],
               ['KARIM BENZEMA', 'ST', 90], ['JOSHUA KIMMICH', 'CDM', 88], ['JAN OBLAK', 'GK', 88],
               ['ANDREAS CHRISTENSEN', 'CB', 83], ['ANDREAS PEREIRA', 'CAM', 77], ['KVARATSKHELIA', 'LW', 86],
               ['BASTONI', 'CB', 85], ['REECE JAMES', 'RB', 84], ['FERLAND MENDY', 'LB', 82],
               ['MIKE MAIGNAN', 'GK', 87], ['NICHOLAS JACKSON', 'ST', 78], ['FRED', 'CDM', 81],
               ['MALACIA', 'LB', 78], ['RICO LEWIS', 'RB', 73]]

for i in player_base:
    i.append(i[2]*100)
    i.append(i[0]+".png")
print(player_base)
