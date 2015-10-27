def azureml_main(frame1):
  import myutilities as mu
 
  numCols = ["Cottagecheese.Prod", "Icecream.Prod", "Milk.Prod", "Total.Prod"]
  ## Call the round2 function in the myutilities script
  frame1[numCols] = frame1[numCols].apply(mu.round2)
  return frame1
