if __name__ == "__main__":
    name = input("name?")
    description = input("bio?")
    photo = input("photo?") 
    formal = "images/members/" + name + " (formal).jpg"
    informal = "images/members/" + name + " (informal).jpg"

    if photo == "n":
        formal = "images/ksea_logo.png"
    if photo == "n":
        informal = "puppy.jpg"
    if description == "n": 
        description = "Hello, I am %s, excited to be a part of KSEA this semester!" % ((name, ))
    
    template =r'''
    <td>
    	<div class="photo photo1">
    		<img data-src="%s" class="initial loaded" src="%s" data-was-processed="true">
    	</div>
    	<div class="photo photo2" style="display: none;">
    		<img data-src="%s">
    	</div>
    	<div class ="segmenttitle"> %s </div>
    	<div class="text bio">
         %s
        </div>
    </td>
    ''' % ((formal, formal, informal, name, description, ))

    print(template)
