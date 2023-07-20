<template>
  <div>
    <div style="display: flex; justify-content: center;">
      <div style="margin: 0 auto;text-align: center;" >
        <el-table
          ref='multipleTable'
          :data='backendData'
          tooltip-effect='dark'
          style='width: 100%;text-align: center;'
          @selection-change='handleSelectionChange'
          :cell-style="rowStyle"
          :header-cell-style="{textAlign: 'center'}"
        >
          <!--表格内列对齐-->
          <el-table-column type='selection' width='55' > </el-table-column>
          <el-table-column  label="商品名称" width="350"  >
            <template slot-scope="scope"><img :src="scope.row.image_url" height="100px"><div><p style="top: 50%;">{{ scope.row.name }}</p></div></template>
          </el-table-column>
          <el-table-column prop='price' label='价格' width='120'> </el-table-column>

          <el-table-column label='操作' width="120">
            <template slot-scope='scope'>
              <el-button
                size='mini'
                type='danger'
                @click='handleDelete(scope.$index, scope.row)'
              >删除</el-button
              >
            </template>
          </el-table-column>
        </el-table>
      </div>
    </div>
    <div style='margin-top: 20px;display: inline-flex'>
      <el-button @click='toggleAllSelection()'>全选</el-button>
      <el-button @click='toggleSelection()'>取消选择</el-button>
<!--      <h3 style="margin-left: 10px;">总金额：{{  totalAmount }}</h3>-->
      <el-button type="primary" style="margin-left: 10px;">提交</el-button>
    </div>
  </div>
</template>
<script>
import axios from "axios";

export default {
  data() {
    return {
      selectedItems: [],
      tableData: [
        {
          date: '2016-05-03',
          name: '王小虎',
          address: 100,
          imageUrl: 'https://imgcdn.kunkunn.cn/7a97b798-66e3-4215-9a96-cfe21dfaa5a1.jpeg'
        },
        {
          date: '2016-05-02',
          name: '王小虎',
          address: 100,
          imageUrl: '#'
        },
        {
          date: '2016-05-04',
          name: '王小虎',
          address: 100,
          imageUrl: '#'
        },
        {
          date: '2016-05-01',
          name: '王小虎',
          address: 100,
          imageUrl: '#'
        },
        {
          date: '2016-05-08',
          name: '王小虎',
          address: 100,
          imageUrl: '#'
        },
        {
          date: '2016-05-06',
          name: '王小虎',
          address: 100,
          imageUrl: '#'
        },
        {
          date: '2016-05-07',
          name: '王小虎',
          address: 100,
          imageUrl: '#'
        }
      ],
      multipleSelection: [],
      backendData: [],
      totalAmount: 0,
    }
  },
  methods: {
    handleDelete(index, row) {
      const id = row.product_id; // 获取当前行的唯一标识，比如ID

      axios.get('/api/remove_cart', { params: { id } })
        .then(response => {
          if (response.data.error) {
            this.$message.error(response.data.error)
            return
          }
          // 删除成功后，从backendData数组中移除对应的行数据
          this.backendData.splice(index, 1)
        })
        .catch(error => {
          this.$message.error('删除商品时出现错误：', error)
        })
    },
    rowStyle() {
      return 'text-align:center'
    },
    toggleSelection(rows) {
      if (rows) {
        rows.forEach((row) => {
          this.$refs.multipleTable.toggleRowSelection(row)
        })
      } else {
        this.$refs.multipleTable.clearSelection()
      }
    },
    toggleAllSelection() {
      this.$refs.multipleTable.toggleAllSelection()
    },
    handleSelectionChange(val) {
      this.selectedItems = val;
      this.selectedTotalAmount = this.calculateSelectedTotalAmount(); // 计算选中项总金额
    },
    calculateSelectedTotalAmount() {
      let total = 0;
      for (const item of this.selectedItems) {
        total += item.price;
      }
      return total;
    },
    handleEdit(index, row) {
      console.log(index, row)
    },
    fetchBackendData() {
      // 调用后端接口获取数据，假设返回的数据是一个数组
      // 示例代码，请根据实际情况修改
      axios.get('/api/cart').then(response => {
        this.backendData = response.data;
      }).catch(error => {
        this.$message.error(error);
      });
    },
  },
  computed: {
    selectedTotalAmount() {
      let total = 0;
      for (const product of this.selectedItems) {
        total += product.price;
      }
      return total.toFixed(2); // 返回保留两位小数的总金额
    },
  },
  mounted() {
    this.fetchBackendData();
    this.totalAmount = this.calculateSelectedTotalAmount(this.selectedItems);
  }

}
</script>
