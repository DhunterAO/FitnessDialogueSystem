function sendTextMessage()
{
    var question = document.getElementById('textBox');
    var url = '/input';
    var data = question.value;
    question.value = '';
    add_question(data);
    $.ajax({
      type: 'POST',
      url: url,
      data: {
        'question': data
      },
      success: function success(response){
        console.log(response);
        add_answer(response)
      }
    });
}

function add_answer(answer)
{
    var conversation_box = document.getElementById('textContext');
    var question_box = document.createElement('li');
    question_box.setAttribute('_v-ba226b7a',"");
    var question_t = document.createElement('div');
    question_t.setAttribute('class',"main");
    question_t.setAttribute('_v-ba226b7a',"");
    var img = document.createElement("img");
    img.setAttribute('class',"avatar");
    img.setAttribute('height','30');
    img.setAttribute('width','30');
    img.setAttribute('src','2.png');
    img.setAttribute('_v-ba226b7a',"");
    var cont = document.createElement('div');
    cont.setAttribute('_v-ba226b7a',"");
    cont.setAttribute('class','text');
    cont.innerHTML = answer;

    question_t.appendChild(img);
    question_t.appendChild(cont);
    question_box.appendChild(question_t);
    conversation_box.appendChild(question_box);
}

function add_question(question)
{
    var conversation_box = document.getElementById('textContext');
    var question_box = document.createElement('li');
    question_box.setAttribute('_v-ba226b7a',"");
    var question_t = document.createElement('div');
    question_t.setAttribute('class',"main self");
    question_t.setAttribute('_v-ba226b7a',"");
    var img = document.createElement("img");
    img.setAttribute('class',"avatar");
    img.setAttribute('height','30');
    img.setAttribute('width','30');
    img.setAttribute('src','1.jpg');
    img.setAttribute('_v-ba226b7a',"");
    var cont = document.createElement('div');
    cont.setAttribute('_v-ba226b7a',"");
    cont.setAttribute('class','text');
    cont.innerHTML = question;

    question_t.appendChild(img);
    question_t.appendChild(cont);
    question_box.appendChild(question_t);
    conversation_box.appendChild(question_box);
}
