<template>
  <div class="login-container">
    <el-form ref="form" :model="form">
      <el-form-item prop="mobile">
        <el-input placeholder="请输入手机号"></el-input>
      </el-form-item>
      <el-form-item>
        <el-input placeholder="请输入密码"></el-input>
      </el-form-item>
      <el-form-item>
        <el-button type="primary">登录</el-button>
        <el-button>重置</el-button>
    </el-form-item>
    </el-form>
  </div>
</template>

<script>
  export default {
    name: "LoginIndex"
  }
</script>

<style scoped>
  .login-container {
    background: url(https://ss1.bdstatic.com/70cFvXSh_Q1YnxGkpoWK1HF6hhy/it/u=191095746,667685191&fm=26&gp=0.jpg) no-repeat;;
    background-size:cover;
    position: fixed;
    top: 0;
    bottom: 0;
    right: 0;
    left: 0;
    display: flex;
    justify-content: center;
    align-items: center;
  }
</style>