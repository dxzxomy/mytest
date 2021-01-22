<template>
  <div>
  <el-container class="layout-container">
    <el-aside
      width="200px"
      class="aside"
    >
      <Aside class="aside-menu"></Aside>
    </el-aside>
    <el-container>
      <el-header class="header">
        <div>
          <i class="el-icon-s-fold"></i>
          <span>简单的后台管理系统</span>
        </div>
        <el-dropdown>
              <div class="avatar-wrap">
<!--                <el-avatar icon="el-icon-user-solid" class="user_img"></el-avatar>-->
                <img src="https://goss4.cfp.cn/creative/vcg/800/new/gic20015026.jpg" alt="" class="avatar">
                <span style="cursor: context-menu;">欧阳梦源</span>
                <i class="el-icon-arrow-down el-icon--right"></i>
              </div>
          <el-dropdown-menu slot="dropdown">
            <el-dropdown-item>个人设置</el-dropdown-item>
            <el-dropdown-item>用户退出</el-dropdown-item>
          </el-dropdown-menu>
      </el-dropdown>
      </el-header>
      <el-main class="main">
        <router-view />
      </el-main>
    </el-container>
  </el-container>
  </div>
</template>

<script>
  import Aside from "./components/Aside";
  export default {
    name: "LayoutIndex",
    components: {Aside},

  }
</script>

<style scoped>
  .layout-container {
    position: fixed;
    left: 0;
    right: 0;
    top: 0;
    bottom: 0;
  }
  .header {
    background: #fff;
    height: 60px;
    justify-content: space-between;
    display: flex;
    align-items: center;
    border-bottom: 1px solid #ccc;

  }
  .aside {
    background-color: #d3dce6;
  }
  .aside-menu {
    border: 0;
    height: 100%;
  }
  .avatar-wrap {
    display: flex;
    align-items: center;
    justify-content: center;
  }
  .avatar{
    width: 40px;
    height: 40px;
    border-radius: 50%;
    margin-right: 6px;
  }
  .main {
    background-color: #e9eef3
  }
</style>