print(r"""

                                         .""--..__
                     _                     []       ``-.._
                  .'` `'.                  ||__           `-._
                 /    ,-.\                 ||_ ```---..__     `-.
                /    /:::\\               /|//}          ``--._  `.
                |    |:::||              |////}                `-. \
                |    |:::||             //'///                    `.\
                |    |:::||            //  ||'                      `|
                /    |:::|/        _,-//\  ||
               /`    |:::|`-,__,-'`  |/  \ ||
             /`  |   |'' ||           \   |||
           /`    \   |   ||            |  /||
         |`       |  |   |)            \ | ||
        |          \ |   /      ,.__    \| ||
        /           `         /`    `\   | ||
       |                     /        \  / ||
       |                     |        | /  ||
       /         /           |        `(   ||
      /          .           /          )  ||
     |            \          |     ________||
    /             |          /     `-------.|
   |\            /          |              ||
   \/`-._       |           /              ||
    //   `.    /`           |              ||
   //`.    `. |             \              ||
  ///\ `-._  )/             |              ||
 //// )   .(/               |              ||
 ||||   ,'` )               /              //
 ||||  /                    /             || 
 `\\` /`                    |             // 
     |`                     \            ||  
    /                        |           //  
  /`                          \         //   
/`                            |        ||    
`-.___,-.      .-.        ___,'        (/    
         `---'`   `'----'`

""")

print("Welcome to Hell Escape!!")
print("Your task is to escape the Grimm Reapers grasp")
input1 = input("You wake up in fiery hellscape, there is a wooden bridge over a river of lava. Type 'cross' to cross, or 'wait' to stay where you are\n").lower()

if input1 == "wait":
  input2 = input("You see a cliff collapse, revealing a hidden passage, which you enter, the passage splits. Type 'left' yo go left, or 'right' to go right.\n").lower()

  if input2 == "left":
    input3 = input("You follow the passage and emerge at a lake of souls. There is a light on the other side. Type 'walk' to walk around the lake, type 'swim' to swim across it.\n").lower()

    if input3 == "walk":
      print("You reached the light you have escaped hell. You are free!")

    elif input3 == "swim":
      print("You sink into the soul of lakes...")
      print(r"""
       _______  _______  _______  _______    _______           _______  _______ 
      (  ____ \(  ___  )(       )(  ____ \  (  ___  )|\     /|(  ____ \(  ____ )
      | (    \/| (   ) || () () || (    \/  | (   ) || )   ( || (    \/| (    )|
      | |      | (___) || || || || (__      | |   | || |   | || (__    | (____)|
      | | ____ |  ___  || |(_)| ||  __)     | |   | |( (   ) )|  __)   |     __)
      | | \_  )| (   ) || |   | || (        | |   | | \ \_/ / | (      | (\ (   
      | (___) || )   ( || )   ( || (____/\  | (___) |  \   /  | (____/\| ) \ \__
      (_______)|/     \||/     \|(_______/  (_______)   \_/   (_______/|/   \__/
      """)

    else:
      print("The Grim Reaper has you now....")
      print(r"""
       _______  _______  _______  _______    _______           _______  _______ 
      (  ____ \(  ___  )(       )(  ____ \  (  ___  )|\     /|(  ____ \(  ____ )
      | (    \/| (   ) || () () || (    \/  | (   ) || )   ( || (    \/| (    )|
      | |      | (___) || || || || (__      | |   | || |   | || (__    | (____)|
      | | ____ |  ___  || |(_)| ||  __)     | |   | |( (   ) )|  __)   |     __)
      | | \_  )| (   ) || |   | || (        | |   | | \ \_/ / | (      | (\ (   
      | (___) || )   ( || )   ( || (____/\  | (___) |  \   /  | (____/\| ) \ \__
      (_______)|/     \||/     \|(_______/  (_______)   \_/   (_______/|/   \__/
      """)

  elif input2 == "right":
    print("The passage collapses...")
    print(r"""
     _______  _______  _______  _______    _______           _______  _______ 
    (  ____ \(  ___  )(       )(  ____ \  (  ___  )|\     /|(  ____ \(  ____ )
    | (    \/| (   ) || () () || (    \/  | (   ) || )   ( || (    \/| (    )|
    | |      | (___) || || || || (__      | |   | || |   | || (__    | (____)|
    | | ____ |  ___  || |(_)| ||  __)     | |   | |( (   ) )|  __)   |     __)
    | | \_  )| (   ) || |   | || (        | |   | | \ \_/ / | (      | (\ (   
    | (___) || )   ( || )   ( || (____/\  | (___) |  \   /  | (____/\| ) \ \__
    (_______)|/     \||/     \|(_______/  (_______)   \_/   (_______/|/   \__/
    """)
    
  else:
    print("The Grim Reaper has you now....")
    print(r"""
     _______  _______  _______  _______    _______           _______  _______ 
    (  ____ \(  ___  )(       )(  ____ \  (  ___  )|\     /|(  ____ \(  ____ )
    | (    \/| (   ) || () () || (    \/  | (   ) || )   ( || (    \/| (    )|
    | |      | (___) || || || || (__      | |   | || |   | || (__    | (____)|
    | | ____ |  ___  || |(_)| ||  __)     | |   | |( (   ) )|  __)   |     __)
    | | \_  )| (   ) || |   | || (        | |   | | \ \_/ / | (      | (\ (   
    | (___) || )   ( || )   ( || (____/\  | (___) |  \   /  | (____/\| ) \ \__
    (_______)|/     \||/     \|(_______/  (_______)   \_/   (_______/|/   \__/
    """)


elif input1 == "cross":
  print("The Grim Reaper cuts the bridge while you cross...")
  print(r"""
   _______  _______  _______  _______    _______           _______  _______ 
  (  ____ \(  ___  )(       )(  ____ \  (  ___  )|\     /|(  ____ \(  ____ )
  | (    \/| (   ) || () () || (    \/  | (   ) || )   ( || (    \/| (    )|
  | |      | (___) || || || || (__      | |   | || |   | || (__    | (____)|
  | | ____ |  ___  || |(_)| ||  __)     | |   | |( (   ) )|  __)   |     __)
  | | \_  )| (   ) || |   | || (        | |   | | \ \_/ / | (      | (\ (   
  | (___) || )   ( || )   ( || (____/\  | (___) |  \   /  | (____/\| ) \ \__
  (_______)|/     \||/     \|(_______/  (_______)   \_/   (_______/|/   \__/
  """)

else:
  print("The Grim Reaper has you now....")
  print(r"""
   _______  _______  _______  _______    _______           _______  _______ 
  (  ____ \(  ___  )(       )(  ____ \  (  ___  )|\     /|(  ____ \(  ____ )
  | (    \/| (   ) || () () || (    \/  | (   ) || )   ( || (    \/| (    )|
  | |      | (___) || || || || (__      | |   | || |   | || (__    | (____)|
  | | ____ |  ___  || |(_)| ||  __)     | |   | |( (   ) )|  __)   |     __)
  | | \_  )| (   ) || |   | || (        | |   | | \ \_/ / | (      | (\ (   
  | (___) || )   ( || )   ( || (____/\  | (___) |  \   /  | (____/\| ) \ \__
  (_______)|/     \||/     \|(_______/  (_______)   \_/   (_______/|/   \__/
  """)


