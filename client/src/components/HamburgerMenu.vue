<template>
    <button class="menu-toggle">
        <div class="hamburger-icon"></div>
    </button>
</template>

<style scoped>
.back-icon {
    width: 0; 
    height: 0; 
    border-top: 10px solid transparent;
    border-bottom: 10px solid transparent; 
    border-right:10px solid black; 
}
.hamburger-icon {
    width: 35px;
    height: 20%;
    background-color: black;
    overflow: visible;
    align-self: center;
    position: relative;
    border-radius: 25px;
}
.hamburger-icon::before {
  content: '';
  display: inline-block;
  position: absolute;
  top: -150%;
  left: 0;
  width: 100%;
  height: 100%;
  background-color: black;
  border-radius: 25px;
}
.hamburger-icon::after {
  content: '';
  display: inline-block;
  position: absolute;
  top: 150%;
  left: 0;
  width: 100%;
  height: 100%;
  background-color: black;
  border-radius: 25px;
}
</style>