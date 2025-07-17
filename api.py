import requests

def main ():
   artist = input("Enter the artist name to search :")
   try:
       response = requests.get(
          "https://api.artic.edu/api/v1/artworks"
          , {"q":artist}                #q is the parameter provided in the documentatiom to search  
                                       # certain items
          
          )
       response.raise_for_status()   #checks the status of the request

   except requests.HTTPError:
      print("Can not execute a query")

   content = response.json()

   
   for artwork in content["data"]:
      print(f"* {artwork['title']}")

main()