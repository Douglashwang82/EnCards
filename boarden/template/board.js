{%extends 'base.html'%}
{% load static %}
{%block title%}Board{%endblock%}
{%block h2%}{%endblock%}
{%block content%}
<style>
h1 { 
    display: block;
    font-size: 5em;
    margin-top: 3em;
    margin-bottom: 0.67em;
    margin-left: 0;
    margin-right: 0;
    font-weight: bold;
}
h4 { 
    display: block;
    font-size: 2em;
    margin-top: 10em;
    
}

</style>
<div id="myCarousel" class="carousel slide" data-ride="carousel" height = 100vh width = 100vw>

  <div class="carousel-inner">
  {% for v,d,e in pack %}
  {%if v.id == first %}
  <div class="carousel-item active" align="center">
    <h1>{{v.vocab}}</h1>
    <h4>{{e}}</h4>
  </div>
  {%else %}
   <div class="carousel-item" align="center">
    <h1>{{v.vocab}}</h1>
    <h4>{{e}}</h4>
  </div>

{% endif %}
{% endfor %}

  

  </div>
  <a class="carousel-control-prev" href="#myCarousel" role="button" data-slide="prev">
    <span class="carousel-control-prev-icon" aria-hidden="true"></span>
    <span class="sr-only">Previous</span>
  </a>
  <a class="carousel-control-next" href="#myCarousel" role="button" data-slide="next">
    <span class="carousel-control-next-icon" aria-hidden="true"></span>
    <span class="sr-only">Next</span>
  </a>
</div>
<script>

$("#myCarousel").carousel({interval: 5000,pause: "false"});


</script>

{%endblock%}
