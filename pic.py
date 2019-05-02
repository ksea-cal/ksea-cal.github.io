if __name__ == "__main__":
    prefix = "bs"
    num_pics = 10
    pic_list = [prefix + str(i) + ".jpg" for i in range(num_pics)]
    curr_text = ""
    for i, pic in enumerate(pic_list):
        template = r'''
        <div class="mySlides fade">
          <div class="numbertext"> %s / %s </div>
          <img src="images_events/%s" style="height:480px" class="center">
        </div>
        ''' % ((str(i + 1), str(num_pics), pic ))
        curr_text += template

    curr_text += r'''
<!-- Next and previous buttons -->
<a class="prev" onclick="plusSlides(-1)">&#10094;</a>
<a class="next" onclick="plusSlides(1)">&#10095;</a>
</div>
<br>
     '''

    curr_text += r'''
<!-- The dots/circles -->
<div style="text-align:center">
     '''

    for i in range(len(pic_list)):
        templ = r'''
        <span class="dot" onclick="currentSlide(%s)"></span>
        ''' % ((str(i + 1), ))

        curr_text += templ

    print(curr_text)
