# Custom Rich Presence
This is the cross-platform program that allows users to change and make custom rich presence without getting confused.

## Installation

First you need python 3(prefer 3.7 and above). Then download files(you can manually download it as zip or use git.) Now `cd` to the directory that you copied/extracted Custom Presence.

```bash
#Windows
pip install -r requirements.txt

#Linux and Mac
pip3 install -r requirements.txt
```

## Usage
### Main page
After installation you can just launch main.py and done. Don't forget to launch Discord while using Custom Presence. Either,you will not able to set custom,beautiful presences.Also,I will make  Exe version and installer for Windows because in Windows it needed to install python while it is pre-installed on Linux and Mac.\
Now in UI(User Interface):\
`ID of RP Application`- As it said,you need to make a RP application on Discord and paste its ID here.You can copy application ID using this button:
![](https://github.com/AzeAstro/RPC-Project/blob/main/images/rp_id.png?raw=true)\
*Check FAQ for more details.*\
`Status` - Can be anything lower than 128 characters.\
`Details` - Can be anything lower than 128 characters.\
`Start time` - This is Epoch(Unix) time that will be used here.UPDATE: **Now epoch converter is available in application UI.**\
`End time` - Same as `Start time` but this time it will show when you will end.(if time passed then it will show `00:00 Left`)\
`Large image's name` - Here you enter the name of the image that you uploaded on the RP application(This app can't upload local images to rich presence.Check FAQ for more details.)\
`Large image's tooltip` - Here you enter tooltip for large image.Here how it will look:\
![](https://github.com/AzeAstro/RPC-Project/blob/main/images/tooltip.png?raw=true)\
`Small image's name` - Same as `Large image` but it will be small(I am aware of that it was dumb sentence.)\
`Small image's tooltip` - same as `Large image's tooltip` but for small image.
### Custom Buttons
Here you set custom buttons.You can make max 2 buttons.(it is Discord side,not me or pypresence). Here is an example:
![](https://github.com/AzeAstro/RPC-Project/blob/main/images/buttons.png?raw=true)\
*Little note:You need to add https:// or http:// on links,either,this link will not count as valid link.*

### Advanced buttons.
It is advanced invites and join buttons. You can use it if you got real details about game. You can use random things for it too but then others will not able to join you.There is how it will look:
![](https://github.com/AzeAstro/RPC-Project/blob/main/images/advanced_invite_preview.png?raw=true)

## Notes
1)Design can be a little bit different on Windows and I will fix UI for Windows too.\
2)Don't forget to add `https://` or `http://` at the beginning of links.\
3)you need to start app first,then you can apply changes. \
4)Rich presence will continue till cmd is open. In Linux and Mac it stops when UI is closed but in Windows not. So,that is why I will make exe version of it.\
5)If fonts look creepy,then you can manually install fonts in `fonts` folder.\
6)You can't use advanced buttons and custom buttons at the same time.

# FAQ
Q:How can I make application on Discord?\
A:First,you need to go to [Discord developer portal](https://discord.com/developers/me).
Then you will see new application button:
![](https://github.com/AzeAstro/RPC-Project/blob/main/images/new_application.png?raw=true)\
Make a new application and name it however you want(in my case,I will name it as Github)
![](https://github.com/AzeAstro/RPC-Project/blob/main/images/naming.png?raw=true)\
Uploading images for rich presence:\
First go to Rich Presence->Art Assets:
![](https://github.com/AzeAstro/RPC-Project/blob/main/images/art_assets.png?raw=true)\
Then there you will see `Upload images` button:\
![](https://github.com/AzeAstro/RPC-Project/blob/main/images/add%20image.png?raw=true)\
Now you can choose images from device. In my case,I will use Github mark.\
Then rename it however you want. It will be needed us in presence if you wanna set images.\
![](https://github.com/AzeAstro/RPC-Project/blob/main/images/name_of_images.png?raw=true)\
Now you need to go to OAuth2 and enable some flags for our application(Don't worry,it is last step.)\
![](https://github.com/AzeAstro/RPC-Project/blob/main/images/rp_oauth2.png?raw=true)\
Now you are ready to use application! Yay!\
\
Q:Will it work on bots?\
A:This app **will not** work on bots. But if you are a developer and want to make custom presence for your bot,then you can use [pypresence](https://github.com/qwertyquerty/pypresence) *for python bots.* There are for other languages too. \
\
Q:Will it work on browser Discord??\
A:No.

## Contributing
Pull requests are welcome. For major changes, please open an issue first to discuss what you would like to change.

Please make sure to update tests as appropriate.

## Used sources:
[PySide2](https://wiki.qt.io/index.php?title=PySide2&redirect=no)\
[Pypresence](https://github.com/qwertyquerty/pypresence)
