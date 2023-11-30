<template>
    <div>
      <h1>策略列表</h1>
      <ul>
        <li v-for="strategy in strategies" :key="strategy.id">
          {{ strategy.name }} - 初始化: {{ strategy.is_initialized ? '是' : '否' }} - 运行中: {{ strategy.is_running ? '是' : '否' }}
        </li>
      </ul>
    </div>
  </template>
  
  <script>
  import axios from 'axios';
  
  export default {
    name: 'HomePage',
    data() {
      return {
        strategies: []
      };
    },
    mounted() {
      axios.get('http://localhost:8000/strategies/')
        .then(response => {
          this.strategies = response.data;
        })
        .catch(error => {
          console.error("加载策略数据时发生错误: ", error);
        });
    }
  };
  </script>
  