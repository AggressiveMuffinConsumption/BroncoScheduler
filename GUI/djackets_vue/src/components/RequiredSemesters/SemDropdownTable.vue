<template>
    <div>
        <table class="shopping">
        <!--<th>2022 Fall</th>-->
        <thead>
            <td colspan="2"><h2>{{ semester }}</h2></td>
        </thead>
        <tbody>
            <tr>
                <!--<td></td><input type="checkbox" id="checkbox" v-model="unchecked" v-on:click="selectTest">
                <label for="checkbox">{{ checked }}</label></td>-->
                <th>Courses</th>
                <th>Units</th>
            </tr>
            <tr style="border-top: 1px solid #aaaaaa">
                <td>CS 4800</td>
                <td>4.00</td>
            </tr>
            <tr>
                <td>&nbsp;</td>
                <td>&nbsp;</td>
            </tr>
        </tbody>
        <tfoot class="foot">
            <tr>
                <td>Total</td>
                <td>&nbsp;</td>
            </tr>
        </tfoot>
        </table>
    </div>
</template>

<script>

export default {
    props: {
        semester: String,
    }
}
</script>

<style scoped>
h2 {
    margin: 0;
}

    h2:first-letter {
        text-decoration: underline;
    }

th, td, tr {
    padding: 10px;
    border: 1px solid #aaaaaa;
}

table {
    background: #ffffff;
    width: 100%;
    margin-top: 25px;
    border: 1px solid #aaaaaa;
    border-collapse: collapse;
}
</style>
