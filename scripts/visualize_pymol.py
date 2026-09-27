from pymol import cmd

cmd.load("figures/EGFR_kinase_best_model.pdb", "egfr_kinase")
cmd.hide("everything")
cmd.show("cartoon")
cmd.spectrum("b", "red_white_blue", "egfr_kinase")  # standart AlphaFold: mavi=yuksek guven
cmd.bg_color("white")
cmd.set("ray_opaque_background", 0)
cmd.orient()
cmd.ray(1200, 900)
cmd.png("figures/EGFR_kinase_pymol_pLDDT.png", dpi=300)

cmd.spectrum("count", "rainbow", "egfr_kinase and name CA")
cmd.ray(1200, 900)
cmd.png("figures/EGFR_kinase_pymol_rainbow.png", dpi=300)
print("PyMOL gorselleri kaydedildi.")
